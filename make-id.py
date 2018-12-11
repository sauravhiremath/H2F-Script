
# coding: utf-8

# In[120]:


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pandas as pd
# import img2pdf


# In[121]:


df = pd.read_csv('data/H2F ID Card Scripting - Sheet1.csv')
names = list(df['name'])
quotes = list(df['quote'])
positions = list(df['position'])


# In[79]:


# font = ImageFont.truetype(<font-file>, <font-size>)
name_font = ImageFont.truetype("data/font/Lato-Black.ttf", 110)
position_font = ImageFont.truetype("data/font/Lato-Regular.ttf", 70)
quote_font = ImageFont.truetype("data/font/Lato-LightItalic.ttf", 40)


# In[127]:


for name,position,quote in zip(names,positions,quotes):
    img = Image.open("data/test.png")

    #For avatar paste (None given in data so...)
    avatar = Image.open('data/avatar.png')
    img.paste(avatar,(310,350),avatar)

    #Data sorting
    draw = ImageDraw.Draw(img)
    first_name,last_name = name.split(' ')

    # Drawing the text on image
    draw.text((73, 1074),first_name,(80, 172, 255),font=name_font)
    draw.text((73, 1200),last_name,(0,0,0),font=name_font)
    draw.text((73, 1320),position,(0,0,0),font=position_font)
    draw.text((73, 1520),quote,(0,0,0),font=quote_font)

    #Saving template as png
    img = img.resize((420,636), Image.ANTIALIAS)
    print('Saving out/ID-Card %s.png'%(name))
    img.save('out/ID-Card %s.png'%(name))

