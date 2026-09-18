import torch; 
def main():
    if(torch.cuda.is_available()):
        print("GPU Pool Active - Batch Embedding/Whisper Ready")  
    else:
        print("CPU-Only Fallback Active.")
