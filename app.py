import streamlit as st
import numpy as np
import matplotlib.image as img_read
from sklearn.cluster import KMeans
import time
from io import BytesIO
from PIL import Image

# --- Intro
st.markdown("## Picfier")
st.write(
    "Welcome to Picfier, the ultimate image color simplifier! This app uses K-means clustering to reduce the number of colors in your images without losing much visual quality for simplified display purposes."
)
st.caption("Picfier works best with ghibli style images and cartoons")


def optimize_image_colors(image_as_3d_array, no_of_colors):
    # Get dimensions
    h, w, c = image_as_3d_array.shape
    image_as_2d_array = image_as_3d_array.reshape(h * w, c)

    # K-means clustering
    kmeans = KMeans(n_clusters=no_of_colors, init="k-means++", random_state=42)
    labels = kmeans.fit_predict(image_as_2d_array)
    cluster_labels = kmeans.cluster_centers_.round(0).astype(int)

    # Map pixels back to their cluster colors
    recolored_image = cluster_labels[labels].reshape(h, w, c)

    return recolored_image.astype(np.uint8)


# Image upload
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "webp", "bmp", "tiff"])
if uploaded_image is not None:
    image_as_3d_array = img_read.imread(uploaded_image)

    no_of_colors = st.slider("Select number of colors", min_value=2, max_value=64, value=8, step=1)

    st.caption("You can choose a higher number colors for subtle compression")

    if st.button("Optimize Image Colors"):
        with st.spinner("Reducing image colors..."):
            recolored_image = optimize_image_colors(image_as_3d_array, no_of_colors)

            # Calculate unique colors
            original_colors = len(np.unique(image_as_3d_array.reshape(-1, 3), axis=0))
            reduced_colors = len(np.unique(recolored_image.reshape(-1, 3), axis=0))

            st.success("Image colors reduced successfully!")
        
        time.sleep(1)
        

        st.write(f"**Original image colors:** {original_colors}")
        st.write(f"**Simplified image colors:** {reduced_colors}")

        # Display original and recolored images
        col1, _, col2 = st.columns([1, 0.05, 1])
        with col1:
            st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
        with col2:
            st.image(recolored_image, caption=f"Simplified Image (no of colors = {no_of_colors})", use_container_width=True)

        # Prepare downloadable image
        buf = BytesIO()
        Image.fromarray(recolored_image).save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Recolored Image",
            data=byte_im,
            file_name="recolored_image.png",
            mime="image/png"
        )
