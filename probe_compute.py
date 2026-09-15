import torch; 
import faiss;
def main():
    if(faiss.cuda.is_available()):
        print("GPU Pool Active - Batch Embedding/Whisper Ready")  
    else:
        print("CPU-Only Fallback Active.")
if __name__ == "__main__":
    main()
