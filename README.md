# Bit-plane_Coder

Every image is made-up of pixels arranged in a matrix. Now lets assume that all the pixels are 8bit pixels meaning each pixel takes 8bits of memory. (Assuming the image is B/W) Now, if we take individual bits from these 8bit sequences. For example a matrix of only the LSB of the 8bits, we get a bit plane.

So, what is the significance of this. Well not all bit planes contribute equally to the overall clarity of the image. The MSB contributes the highest, and it reduces and LSB contributes the least. So even if we completely change the LSB bits of all the pixels in an image we can barely tell the difference with our naked eye.

So, we completely change the LSB bit-plane !!

And what do we put in it? Well whatever data we want. In this code I have coded a text file to be hidden in this layer.

### Usage

#### Coder
For using the code follow the steps:
1. Get a image that you want to code data into (Doesn't need to be a B/W image but the ouput will be so better start with one. Also higher the resolution more data you can store.)
2. In the "message.txt" write the stuff that you want to code into the image. (The last character of the code must be a '@' and do not use '@' in your secret code)
3. In the Coder.py, change the imagepath and filename as required.
4. Run Coder.py. It will make a image called "coded.png". 

#### Decoder
For using the code follow the steps:
1. Get the image that is already coded.
2. Make a txt file where you want the code to be saved into
3. Give the correct imagepath and filepath for the two files in Decoder.py
4. Run Decoder.py. It will update the txt file with any code that is hidden within.


### Future Plans:
This is still an active project. There are many features that I want to add like a UI for the code and RGB support where different data can be coded into R,G and B layers seperately.
Stay tuned for any updates.

Cheers

-HimaSava