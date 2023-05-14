import os
import re

def remove_unnecessary_characters(file_name):
    # Remove square brackets and their contents
    file_name = re.sub(r'\[[^]]*\]', '', file_name)
    
    # Remove parentheses and their contents
    file_name = re.sub(r'\([^)]*\)', '', file_name)
    
    # Remove multiple spaces and leading/trailing spaces
    file_name = re.sub(r' +', ' ', file_name).strip()
    
    return file_name

def extract_episode_number(file_name):
    # Find the last occurrence of a sequence of digits
    episode_number = re.search(r'\b(\d+)\b', file_name[::-1])
    if episode_number:
        episode_number = episode_number.group(1)
        # Reverse the episode number back to the correct order
        episode_number = episode_number[::-1]
        return episode_number
    return None

def correct_file_name(file_path):
    if file_path.endswith(("mkv", "mp4", "flv", "wmv", "avi", "mpg", "mpeg", "mp3", "avi", "dat")):
        file_name, file_extension = os.path.splitext(file_path)
        
        # Remove unnecessary characters from the file name
        new_file_name = remove_unnecessary_characters(file_name)
        
        # Extract the episode number from the file name
        episode_number = extract_episode_number(new_file_name)
        
        if episode_number:
            # Split the file name into components
            components = new_file_name.split('-')
            
            # Remove leading and trailing spaces from each component
            components = [component.strip() for component in components]
            
            # Remove empty components
            components = [component for component in components if component]
            
            # Check if the episode number is already present in the file name
            if episode_number not in components[-1]:
                # Add the episode number to the last component
                components[-1] = f"{components[-1]} - {episode_number}"
            
            # Reconstruct the new file name
            new_file_name = ' - '.join(components) + file_extension
            
            return new_file_name
    
    return None

path = "."
for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)
    new_file_name = correct_file_name(file_path)
    if new_file_name and new_file_name != file_name:
        new_file_path = os.path.join(path, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed: {file_name} => {new_file_name}")
