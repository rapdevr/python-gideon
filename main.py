from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertModel
from ast import literal_eval
import pandas as pd
import json
import pickle as pkl
import requests
import urllib.request
import tensorflow as tf

# create the tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

# load in the dataset
url = 'https://github.com/Robert-MacWha/Project-Aurras/blob/27e95578b610699ece51fc8d2f183c03aa09ca15/dataset/train.pkl'

with open("train.pkl", "rb") as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
df.to_csv(r'train.csv')

df_train = pd.read_csv('train.csv')
# load json data
urljson = 'https://raw.githubusercontent.com/Robert-MacWha/Project-Aurras/main/dataset/intent_labels.json'
resp = requests.get(urljson)
intent_labels = json.loads(resp.text)
intent_count = len(intent_labels)

# using tokenizer to convert the text into numeric input IDs

inputs = tokenizer(
    list(df_train['word_entities']),      # specify the string[] to tokenize
    max_length=128,               # custom padding
    padding='max_length',         # sets padding to the custom value
    return_attention_mask=True,
    return_token_type_ids=False,
    return_tensors='np'           # flag to return numpy array
)
x_train_ids = inputs['input_ids']
x_train_attention = inputs['attention_mask']


# example of a single sentence after tokenization

print(x_train_ids)
# first 7 are etxt IDs, rest are padding*

print(x_train_attention)
# ones represent parts of the sentence, zeroes represent padded tokens

# convert the y_labels into one-hot* labels using tensorflow built-in function
y_train_intents = tf.one_hot(df_train['prompt_intent'].values, intent_count)

# sample datapoint
print(f'Prompt:         {df_train["word_entities"][0]}')
print(f'Token IDs:      {x_train_ids[0][:12]}...')
print(f'Attention mask: {x_train_attention[0][:12]}...')
print(f'One-hot Label:  {y_train_intents[0]}')
# Prompt: can you calculate twelve point five plus two Token
# IDs: [101 2064 2017 18422 4376 2391 2274 4606 2048, 102 0 0]... 
# Attention mask: [1 1 1 1 1 1 1 1 1 1 0 0]... 
# One-hot Label: [1. 0. 0. 0. 0.]

# define the input layers
input_ids_layer = tf.keras.layers.Input(
    shape=(128,),       # shape value matches value of padding used earlier
    name='input_ids',
    dtype='int32',
)

input_attention_layer = tf.keras.layers.Input(
    shape=(128,),
    name='input_attention',
    dtype='int32',
)

#create the pre-trained model
transfomer = TFDistilBertModel.from_pretrained('distilbert-base-uncased')

#feed the inputs into the pre-trained model
#results in a layer of shape 

last_hidden_state = transfomer([
    input_ids_layer,
    input_attention_layer])[0]

# the cls token contains a condensed representation of the entire last_hidden_state tensor
cls_token = last_hidden_state[:, 0, :]

weight_initializer = tf.keras.initializers.GlorotUniform()

# create the output layer
intent_output = tf.keras.layers.Dense(
    intent_count,
    activation='softmax',
    kernel_initializer=weight_initializer, # type: ignore
    kernel_constraint=None,
    bias_initializer='zeros',
    name='intent_output'
)(cls_token)


#define the model
model = tf.keras.Model(
    [input_ids_layer, input_attention_layer],
    [intent_output])

print(model.summary())

model.compile(
    optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5),
    loss      = tf.keras.losses.CategoricalCrossentropy(),
    metrics   = [tf.keras.metrics.CategoricalAccuracy('categorical_accuracy')])

#train the model
history = model.fit(
    x = [x_train_ids, x_train_attention],
    y = [y_train_intents],
    epochs = 2,
    batch_size = 16,
    verbose = 1
)

while True:
    # Get user input
    user_input = input("Please enter a sentence: ")

    # Convert user input to token IDs and attention mask
    user_input_tokens = tokenizer(
        user_input,
        max_length=128,
        padding='max_length',
        return_attention_mask=True,
        return_token_type_ids=False,
        return_tensors='tf'
    )
    user_input_ids = user_input_tokens['input_ids']
    user_input_attention = user_input_tokens['attention_mask']

    # Make prediction
    prediction = model.predict([user_input_ids, user_input_attention])
    predicted_label = intent_labels[str(tf.argmax(prediction, axis=1).numpy()[0])]

    # Print result
    print(f"Predicted intent: {predicted_label}\n")