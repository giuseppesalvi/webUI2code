# Web UI code generation: a transformer-based model applied to real-world screenshots
This repository contains the code for my Master's Degree Thesis in Computer Engineering at Politecnico di Torino.

[Link](https://webthesis.biblio.polito.it/28535/) to the thesis.
[This](https://github.com/giuseppesalvi/webUI2code/blob/main/Summary_Web_UI_code_generation__a_transformer_based_model_applied_to_real_world_screenshots.pdf) file contains the summary of the thesis.

## Website screenshot and code extraction tool
The tool utilized in the initial phase of the thesis for extracting screenshots and code from websites to create **WebUI2Code** Dataset can be found here [Website screenshot and code getter](https://github.com/giuseppesalvi/website-screenshot-and-code-getter).

## Repository structure
- **notebooks**: Contains the code used during the training and testing phases of the model on various datasets, as well as the results analysis.
- **results**: Contains the predictions and answers for the test set in a zip format for each conducted experiment.
- **utils**: Contains the code for post-processing results and extracting website screenshots.

## Datasets

Datasets employed in the thesis are provided below:
-  [Pix2Code web](https://drive.google.com/file/d/1upfkF-nU76Hkwhk7BvmEhHpDIldRquqL/view?usp=sharing)
-  [Pix2Code web - HTML](https://drive.google.com/file/d/1RpiKpdVAPWt-cSlRkt02_rzl1ZbOyPLP/view?usp=sharing)
-  [Pix2Code web - HTML Lorem Ipsum](https://drive.google.com/file/d/1lc0-Wcaoyr_EsB3QXUjQCxGSXyVeDVJ5/view?usp=sharing)
-  [Synthetic Bootstrap Dataset - mini](https://drive.google.com/file/d/1--Z8OU67XpznBM5IEI7BXPW5fYUZaF3J/view?usp=sharing)
-  [Synthetic Boostrap Dataset](https://drive.google.com/file/d/1-0r3fZFN4-hm1xsoODlMBRMipDG8doW_/view?usp=share_link)
-  [Synthetic Bootstrap Dataset - Sketch](https://drive.google.com/file/d/1_etxk62xKSmrSZkqQ0w31k8noF1n95D6/view?usp=share_link)
-  [UI2Code - 10000](https://drive.google.com/file/d/1TytVGqLqHJf8CXMXKNh8R0Y4lD-wqwa0/view?usp=sharing)
-  [**WebUI2Code**](https://drive.google.com/file/d/1gzU4umU9x--qRGlGIE7lpNTdKkPkrKGa/view?usp=share_link)
-  [WebUI2Code - preprocessed textual files](https://drive.google.com/file/d/1gzU4umU9x--qRGlGIE7lpNTdKkPkrKGa/view?usp=share_link)
-  [WebUI2Code - 4096](https://drive.google.com/file/d/1gzU4umU9x--qRGlGIE7lpNTdKkPkrKGa/view?usp=share_link)
-  [WebUI2Code - 4096 Lorem Ipsum](https://drive.google.com/file/d/101bNSbU49oToe6fraQL9Z-bRDcB5KJ6V/view?usp=sharing)

Here are the lists of files from **WebUI2Code** Dataset under different thresholds:
- [WebUI2Code - 4096](https://drive.google.com/file/d/1DEiICQ7UIpERliLeLWnpv5dyUNE8uOab/view?usp=share_link)
- [WebUI2Code - 8192](https://drive.google.com/file/d/12WbMzGFOcdU-j8NgVBN_uQBqEGHUs5Hz/view?usp=sharing)
- [WebUI2Code - 12288](https://drive.google.com/file/d/1JoSvJUnSqCsJ6r5mis6PSK1oB_1G4RRg/view?usp=sharing)
- [WebUI2Code - 16384](https://drive.google.com/file/d/1IuV0JOFhCrXGImRmEMUD8Ve8uiDcoPhb/view?usp=sharing)
- [WebUI2Code - 20834](https://drive.google.com/file/d/16gqbrbo9WoItfiyofeajLi44gWZnfy1h/view?usp=sharing)
- [WebUI2Code - 24576](https://drive.google.com/file/d/16gqbrbo9WoItfiyofeajLi44gWZnfy1h/view?usp=sharing)
- [WebUI2Code - 28672](https://drive.google.com/file/d/1p32i6tB4UQQSqaOyhQ3a8qfF6LEl7yrP/view?usp=sharing)
- [WebUI2Code - 32768](https://drive.google.com/file/d/1p32i6tB4UQQSqaOyhQ3a8qfF6LEl7yrP/view?usp=sharing)
- [WebUI2Code - 36864](https://drive.google.com/file/d/1x59I3M75FAI-GQcoXENv6ISTkccPs2rD/view?usp=share_link)
- [WebUI2Code - 40960](https://drive.google.com/file/d/1x59I3M75FAI-GQcoXENv6ISTkccPs2rD/view?usp=share_link)
- [WebUI2Code - above 40960](https://drive.google.com/file/d/19pvRCNjOvNBFdoLVQYDcTtmjQUv3gGst/view?usp=sharing)

## Model Checkpoints
Checkpoints for the Pix2Struct model trained during the experiments are available at:
- [Pix2Code web](https://drive.google.com/file/d/1-EIVjOSfma3FW2i5OKobMOqRwsqstDsV/view?usp=share_link)
- [Pix2Code web - HTML](https://drive.google.com/file/d/1-YFzRDn0S5drxqrviHY-52sD9cMzcChQ/view?usp=share_link)
- [Pix2Code web - HTML - FULL](https://drive.google.com/file/d/1-YFzRDn0S5drxqrviHY-52sD9cMzcChQ/view?usp=share_link)
- [Pix2Code web - HTML Lorem Ipsum](https://drive.google.com/file/d/1-fwtr-cawz3XhyqIsMzei3vL7v6kfyLQ/view?usp=share_link)
- [Pix2Code web - HTML Lorem Ipsum - FULL ](https://drive.google.com/file/d/10In5amVgHWzcOWpOrL8zrcfJYUEXnp0f/view?usp=share_link)
- [Synthetic Bootstrap Dataset - mini](https://drive.google.com/file/d/1-FvnPAwYkbjs-2Te2l5F5tv-erq0CY_H/view?usp=share_link)
- [Synthetic Boostrap Dataset](https://drive.google.com/file/d/10C_oPG_MjDhG1FE2xhHkFTVpLprcAqo8/view?usp=share_link)
- [Synthetic Bootstrap Dataset - Sketch](https://drive.google.com/file/d/1-aa_tALRhnZWAeZhj22LnrPRnVxZu3Hq/view?usp=share_link)
- [RICO](https://drive.google.com/file/d/1-mbM30KKQAdW9DuyfpdhnX9jVJZJoW4U/view?usp=share_link)
- [UI2Code - 10000](https://drive.google.com/file/d/1-TGclNYmmtJKiZMqX6AdTLzyMJyP81ul/view?usp=share_link)
- [WebUI2Code](https://drive.google.com/file/d/1-8nNGVNjXyuNBkp3UOYzfMEOMfQccxGg/view?usp=share_link)
- [WebUI2Code - 4096](https://drive.google.com/file/d/1-QLwUqBxt8RKgJuy-6VHnOH5M1Ank3vF/view?usp=share_link)
- [WebUI2Code - 4096 - FULL](https://drive.google.com/file/d/1-S4W-EwAKWvzoA42NXqCF22nYJ1x94gs/view?usp=share_link)
- [WebUI2Code - 4096 - 512](https://drive.google.com/file/d/1-Xmd8UxSY1iOZU_t5856HXW57G2WC8UL/view?usp=share_link)
- [WebUI2Code - 4096 Lorem Ipsum](https://drive.google.com/file/d/1-ZbKZSqXD9rYBtnkETRDsgWG3195HYhs/view?usp=share_link)

## Acknowledgements
- [HuggingFace Transformer library](https://github.com/huggingface/transformers)
- [Pix2Struct model](https://github.com/google-research/pix2struct/tree/main)
- [WebGenerator](https://github.com/agsoto/webgenerator)
- [Pix2Code](https://github.com/tonybeltramelli/pix2code)
- [Pix2Code Pytorch](https://github.com/timoangerer/pix2code-pytorch)
- [RICO](http://www.interactionmining.org/rico.html)
- [UI2Code](https://github.com/ccywch/UI2code/tree/master)
  
