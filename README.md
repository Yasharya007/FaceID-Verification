
# Face Verification Using Siamese Neural Networks

## Overview
This project implements Siamese Neural Network (SNN) for face verification using the Labeled Faces in the Wild (LFW) dataset. The model learns a similarity metric to verify whether two face images belong to the same person.
The model is implemented in Python kivi app for faceid verification.

---

## Requirements

### 1. Software Prerequisites
Ensure you have the following installed on your system:
- Python 3.7 or later
- Jupyter Notebook or Jupyter Lab

#### Required Libraries:
- TensorFlow (>=2.6.0)
- NumPy
- Matplotlib
- scikit-learn
- OpenCV
- Pandas
- kivy

---

## Dataset

### Download the Labeled Faces in the Wild (LFW) Dataset
1. Visit the [LFW dataset page](http://vis-www.cs.umass.edu/lfw/).
2. Download the dataset:
   - **LFW Images:** `lfw.tgz`.

---

## File Structure
Below is the directory structure for the project:
```plaintext
FaceID-Verification/
├── app/                      # Python app for faceid verification
    ├── Application_Data/              # Application Data
        ├── Input_image                   # Store input image to verify
        ├── Verification_Images           # Store refrence images
    ├── faceid.py                      # faceid verification app
    ├── layers.py                      # Distance calculator
├── data/                      # Directory for LFW dataset
    ├── anchor                         # store anchor images
    ├── negative                       # store negative images
    ├── negative                       # store positive images
├── Siamese Model Facial Verification Training.ipynb  #Jupyter notebook for model training
├── README.md                  # Project documentation
├── Application_data/          # Application data
    ├── Input_image                    # Store input image to verify
    ├── Verification_Images            # Store refrence images
```

---

## Running the Project
### Model Training
1. **Launch Jupyter Notebook**
   Open a terminal in the project root directory and run:
   ```bash
   jupyter notebook
   ```

2. **Open the Notebook**
   In the Jupyter Notebook interface, navigate to and open the file:
   `Siamese Model Facial Verification Training.ipynb`.

3. **Execute the Cells**
   Run each code cell sequentially to:
   - Load and preprocess the dataset.
   - Define and train the Siamese Neural Network.
   - Evaluate the model.

4. **View Results**
   Results, such as training accuracy, loss curves, and test performance, will be displayed within the notebook.

### Faceid Verification app
1. **Add Reference Image**
   In /app/Application_data/Verification_Images add 20-30 sample images for reference to verify.
2. **Import saved model**
   copy the saved model(.h5 file) in app directory.
3. **Run App**
   Open 'app' folder in VS Code and execute following command in terminal :
   ```bash
   python faceid.py
   ```
---

## Key Notes

- **GPU Support:** If you have a compatible GPU, ensure TensorFlow is configured to utilize it for faster training. Follow [TensorFlow GPU Setup Guide](https://www.tensorflow.org/install/gpu) for more information.
- **Adjust Parameters:** You can modify the batch size, number of epochs, and learning rate in the training configuration cells.
- **Data Path:** Ensure the dataset is correctly placed in the `data/` directory as the notebook relies on this structure.

---

## Authors
This project was developed by Yash Arya. See the project report for details on contributions.
