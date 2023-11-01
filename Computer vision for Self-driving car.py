# %%
#importing the libraries 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# %%
#importing the images for operations 
image_color = mpimg.imread ('C:/Users/User/Documents/SELF DRIVING CAR/IMG/center_2023_07_24_20_43_42_827.jpg')
plt.imshow(image_color)

# %%
image_color.shape

# %%
#now we will convert it into gray scale 
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap = 'gray')

# %%
image_gray.shape

# %%
#Road marking detection
image_color = mpimg.imread ('C:/Users/User/Documents/SELF DRIVING CAR/IMG/center_2023_07_24_20_43_42_827.jpg')
plt.imshow(image_color)

# %%
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap = 'gray')

# %%
image_copy = np.copy(image_gray)

# %%
image_copy [ (image_copy[:,:]) < 250 ] = 0

# %%
plt.imshow(image_copy, cmap = 'gray')
plt.show()

# %%
#COLOR SPACE MANIPULATION
image = cv2.imread ('C:/Users/User/Documents/SELF DRIVING CAR/IMG/center_2023_07_24_20_43_42_827.jpg')

# %%
image.shape

# %%
#Printing the Height and the Width of the image 
print('Height = ', int(image.shape[0]), 'pixels')
print('Width = ', int(image.shape[1]), 'pixels')

# %%
cv2.imshow('Self Driving Car!', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
#Plotting the image
plt.imshow(image)
image.shape

# %%



