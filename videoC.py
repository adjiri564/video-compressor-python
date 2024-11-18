# import tkinter as tk  
# import traceback  
# from tkinter import filedialog, messagebox, ttk  
# import cv2  

# def compress_video(input_file, output_file, scale_percent=50):  
#     """Compress video by resizing it to a specified percentage of the original dimensions."""  
#     cap = cv2.VideoCapture(input_file)  
#     if not cap.isOpened():  
#         print("Error: Could not open video.")  
#         return  
    
#     # Get original dimensions  
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  
    
#     # Calculate new dimensions  
#     new_width = int(width * scale_percent / 100)  
#     new_height = int(height * scale_percent / 100)  

#     # Define codec and create VideoWriter object  
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or use 'XVID' for .avi  
#     out = cv2.VideoWriter(output_file, fourcc, cap.get(cv2.CAP_PROP_FPS), (new_width, new_height))  

#     total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  
#     processed_frames = 0  

#     while True:  
#         ret, frame = cap.read()  
#         if not ret:  
#             break  
#         # Resize the frame  
#         frame_resized = cv2.resize(frame, (new_width, new_height))  
#         # Write the frame into the new video file  
#         out.write(frame_resized)  
#         processed_frames += 1  
#         # Update progress bar  
#         progress_bar['value'] = (processed_frames / total_frames) * 100  
#         root.update_idletasks()  # Refresh GUI  

#     # Release everything  
#     cap.release()  
#     out.release()  
#     print("Video compression complete.")  
#     messagebox.showinfo("Success", "Video compressed successfully!")  # Notify success  

# def select_input_file():  
#     """Open file dialog to select input video file."""  
#     global file_path  # Declare file_path as global  
#     file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])  
#     if file_path:  
#         input_canvas.delete("all")  # Clear previous content  
#         input_canvas.create_text(10, 10, anchor="nw", text=file_path, fill="black")  # Display file path  

# def launch_compression():  
#     """Trigger video compression."""  
#     global file_path  # Access the global file_path  
#     if file_path:  
#         output_path = file_path.rsplit(".", 1)[0] + "_compressed.mp4"  # Automatically generate output file name  
#         compress_video(file_path, output_path)  
#         progress_bar['value'] = 0  # Reset progress bar after compression  
#     else:  
#         messagebox.showwarning("Input Error", "Please select an input file.")  

# # Create the main window  
# root = tk.Tk()  
# root.title("Video Compressor")  

# # Create input file selection  
# input_label = tk.Label(root, text="Input Video File:")  
# input_label.pack(pady=5)  
# input_canvas = tk.Canvas(root, width=400, height=30, bg="white")  # Use Canvas for drag and drop  
# input_canvas.pack(pady=5)  
# input_button = tk.Button(root, text="Browse", command=select_input_file)  
# input_button.pack(pady=5)  

# # Create compress button  
# compress_button = tk.Button(root, text="Compress Video", command=launch_compression)  
# compress_button.pack(pady=20)  

# # Create progress bar  
# progress_bar = ttk.Progressbar(root, length=300, mode='determinate')  
# progress_bar.pack(pady=10)  

# # Start the GUI event loop  
# root.mainloop()

import tkinter as tk  
import traceback  
from tkinter import filedialog, messagebox, ttk  
import cv2  

def compress_video(input_file, output_file, scale_percent=50):  
    """Compress video by resizing it to a specified percentage of the original dimensions."""  
    cap = cv2.VideoCapture(input_file)  
    if not cap.isOpened():  
        print("Error: Could not open video.")  
        return  
    # Get original dimensions  
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  
    # Calculate new dimensions  
    new_width = int(width * scale_percent / 100)  
    new_height = int(height * scale_percent / 100)  
    # Define codec and create VideoWriter object  
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or use 'XVID' for .avi  
    out = cv2.VideoWriter(output_file, fourcc, cap.get(cv2.CAP_PROP_FPS), (new_width, new_height))  
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  
    processed_frames = 0  
    while True:  
        ret, frame = cap.read()  
        if not ret:  
            break  
        # Resize the frame  
        frame_resized = cv2.resize(frame, (new_width, new_height))  
        # Write the frame into the new video file  
        out.write(frame_resized)  
        processed_frames += 1  
        # Update progress bar  
        progress_bar['value'] = (processed_frames / total_frames) * 100  
        root.update_idletasks()  # Refresh GUI  
    # Release everything  
    cap.release()  
    out.release()  
    print("Video compression complete.")  
    messagebox.showinfo("Success", "Video compressed successfully!")  # Notify success  

def select_input_file():  
    """Open file dialog to select input video file."""  
    global file_path  # Declare file_path as global  
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])  
    if file_path:  
        input_canvas.delete("all")  # Clear previous content  
        input_canvas.create_text(10, 10, anchor="nw", text=file_path, fill="black")  # Display file path  

def launch_compression():  
    """Trigger video compression."""  
    global file_path  # Access the global file_path  
    if file_path:  
        output_path = file_path.rsplit(".", 1)[0] + "_compressed.mp4"  # Automatically generate output file name  
        compress_video(file_path, output_path)  
        progress_bar['value'] = 0  # Reset progress bar after compression  
    else:  
        messagebox.showwarning("Input Error", "Please select an input file.")  

# Create the main window  
root = tk.Tk()  
root.title("Video Compressor")  
root.geometry("500x300")  # Set window size  
root.configure(bg="#f0f0f0")  # Set background color  

# Create a frame for input selection  
input_frame = tk.Frame(root, bg="#f0f0f0")  
input_frame.pack(pady=20)  

input_label = tk.Label(input_frame, text="Input Video File:", bg="#f0f0f0", font=("Arial", 12))  
input_label.pack(pady=5)  

input_canvas = tk.Canvas(input_frame, width=400, height=30, bg="white", highlightbackground="#cccccc")  
input_canvas.pack(pady=5)  

input_button = tk.Button(input_frame, text="Browse", command=select_input_file, bg="#4CAF50", fg="white", font=("Arial", 10))  
input_button.pack(pady=5)  

# Create a frame for compression button and progress bar  
compress_frame = tk.Frame(root, bg="#f0f0f0")  
compress_frame.pack(pady=20)  

compress_button = tk.Button(compress_frame, text="Compress Video", command=launch_compression, bg="#2196F3", fg="white", font=("Arial", 12))  
compress_button.pack(pady=10)  

# Create progress bar  
progress_bar = ttk.Progressbar(compress_frame, length=300, mode='determinate')  
progress_bar.pack(pady=10)  

# Start the GUI event loop  
root.mainloop()