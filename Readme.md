# Melody4U
Sphinx Hackathon Project
Welcome to our music recommendation system! We utilize a multi-faceted approach to deliver personalized song recommendations to users, ensuring a delightful listening experience. Below, we outline the key components and methodologies that power our recommendation engine.

## 1. Demography-Based Recommendations

Our system takes into account user demographics to provide recommendations tailored to individual preferences. Demographic information helps in understanding the general preferences of users, such as age, location, and gender.

## 2. Previous Listening History

We analyze a user's past listening history, taking into consideration factors like genre, artist, and user preferences derived from their likes and dislikes of songs. This historical data forms the foundation for understanding a user's musical taste.

## 3. Short Clip Features and ELO Rating Algorithm

We present users with short audio clips of songs, creating 10 pairs for comparison. This unique approach allows us to assess user preferences in terms of emotions and genre. The ELO rating algorithm, widely used in ranking systems, is employed to continuously adapt and modify recommendations.

## 4. Recommendation Engine

Our recommendation engine is the heart of the system. It processes a user's history and generates weights for song attributes, including artist, genre, and user preference. These weights are used to generate the top 5 song recommendations that align with the user's musical tastes.

## 5. Genre Classification with CNN and Emotion Classification with RoberTa

We employ Convolutional Neural Network (CNN) models with attention layers for genre classification. This approach achieves a remarkable F1 score of 0.88, ensuring accurate genre identification. For emotion classification, we utilize RoberTa, a fine-tuned model that considers both audio and lyrics to classify emotions, providing users with emotionally resonant music recommendations.

## 6. Custom YouTube Playlists

As the final step, our system creates custom private YouTube playlists for users, seamlessly integrating our recommendations. Please note that this feature is currently in invite-only access due to YouTube Data API restrictions. To request access for testing, kindly contact us at somshuvra.online@gmail.com.

## Get Started

To start exploring our music recommendation system, follow the setup and installation instructions in our [Installation Guide](installation.md).

We are dedicated to providing you with the best music recommendations, continually improving our algorithms, and expanding our services. Your feedback is invaluable to us, so please feel free to reach out with any questions or suggestions.

Enjoy your personalized music journey with us!

For inquiries and support, contact: somshuvra.online@gmail.com
