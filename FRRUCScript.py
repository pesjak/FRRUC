import os
import re

def remove_unnecessary_characters(file_name):
    # Remove square brackets and their contents
    file_name = re.sub(r'\[[^\]]*\]', '', file_name)
    
    # Remove parentheses and their contents
    file_name = re.sub(r'\([^)]*\)', '', file_name)
    
    # Remove multiple spaces and leading/trailing spaces
    file_name = re.sub(r' +', ' ', file_name).strip()
    
    return file_name

def extract_episode_number(file_name):
    # Find the first occurrence of a sequence of digits
    episode_number = re.search(r'\b(\d+)\b', file_name)
    if episode_number:
        return episode_number.group(1)
    return None

def correct_file_name(file_path):
    if file_path.endswith(("mkv", "mp4", "flv", "wmv", "avi", "mpg", "mpeg", "mp3", "avi", "dat")):
        file_name, file_extension = os.path.splitext(file_path)
        
        # Remove unnecessary characters from the file name
        new_file_name = remove_unnecessary_characters(file_name)
        
        # Extract the episode number from the file name
        episode_number = extract_episode_number(new_file_name)
        
        if episode_number:
            # Remove the episode number from the file name
            new_file_name = re.sub(r'\b\d+\b', '', new_file_name).strip()
            
            # Construct the new file name with the episode number and extension
            new_file_name = f"{new_file_name} - {episode_number}{file_extension}"
            return new_file_name
    
    return None

path = "."
for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)
    new_file_name = correct_file_name(file_path)
    if new_file_name:
        new_file_path = os.path.join(path, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed: {file_name} => {new_file_name}")
