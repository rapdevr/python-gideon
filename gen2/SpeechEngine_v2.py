#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


# Trainer: where stuff actually happens
# TrainingArgs: defines the set of arguments of the Trainer.
from trainer import Trainer, TrainerArgs


# In[3]:


# GlowTTSConfig: all model related values for training, validating and testing.
from TTS.tts.configs.glow_tts_config import GlowTTSConfig


# In[4]:


# BaseDatasetConfig: defines name, formatter and path of the dataset
from TTS.tts.configs.shared_configs import BaseDatasetConfig
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.glow_tts import GlowTTS
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.utils.audio import AudioProcessor


# In[5]:


# using the same path as the notebook in the gen2 folder
output_path = os.path.dirname(os.path.abspath("/output"))


# In[6]:


#DEFINE DATASET CONFIG
# set my dataset as the target and define the path
dataset_config = BaseDatasetConfig(
    formatter="ljspeech", meta_file_train=r"C:\Users\rishi\Documents\GitHub\K.A.I\gen2\GidSpeechset\metadata.csv", path=os.path.join(output_path, r"C:\Users\rishi\Documents\GitHub\K.A.I\gen2\output"))


# In[7]:


# INITIALIZE THE TRAINING CONFIGURATION
# configure the model. Every config class inherits the BaseTTSConfig
config = GlowTTSConfig(
    batch_size=32,
    eval_batch_size=16,
    num_loader_workers=4,
    num_eval_loader_workers=4,
    run_eval=True,
    test_delay_epochs=-1,
    epochs=1000,
    text_cleaner="phoneme_cleaners",
    use_phonemes=True,
    phoneme_language="en-us",
    phoneme_cache_path=os.path.join(output_path, "phoneme_cache"),
    print_step=25,
    print_eval=False,
    mixed_precision=True,
    output_path=output_path,
    datasets=[dataset_config],
)


# In[8]:


#INITIALIZE THE AUDIO PROCESSOR
# Audio processor is used for feature extraction and audio I/O.
# It mainly serves to the dataloader and the training loggers.
ap = AudioProcessor.init_from_config(config)


# In[9]:


# INITIALIZE THE TOKENIZER
# Tokenizer is used to convert text to sequences of token IDs.
# If characters are not defined in the config, default characters are passed to the config
tokenizer, config = TTSTokenizer.init_from_config(config)


# In[10]:


# LOAD DATA SAMPLES
# Each sample is a list of '''[text, audio_file_path, speaker_name]'''
# You can define your custom sample loader returning the list of samples.
# Or define your own custom formatter and pass it to the 'load_tts_samples'.
train_samples, eval_samples = load_tts_samples(
    dataset_config,
    eval_split=True,
    eval_split_max_size=config.eval_split_max_size,
    eval_split_size=100,
)


# In[11]:


# INITIALIZE THE MODEL
# Models take a config object and speaker manager as input
# Config define the details of the model like the number of layers, the size of the embedding, etc.
# Speaker manager is used by multi-speaker models.
model = GlowTTS(config, ap, tokenizer, speaker_manager=None)


# In[13]:


# INITIALIZE THE TRAINER
# Trainer provides a generic API to train all TTS models with all perks like mixed-precision training,
# Distributed training, etc.
trainer = Trainer(
TrainerArgs(), config, output_path, model=model, train_samples=train_samples, eval_samples=eval_samples
)

# AND... 3,2,1...
trainer.fit()


# In[ ]:




