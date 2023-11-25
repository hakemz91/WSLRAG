import os

# from dotenv import load_dotenv
from chromadb.config import Settings

# https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/excel.html?highlight=xlsx#microsoft-excel
from langchain.document_loaders import CSVLoader, PDFMinerLoader, TextLoader, UnstructuredExcelLoader, Docx2txtLoader


# load_dotenv()
ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Define the folder for storing database
SOURCE_DIRECTORY = f"{ROOT_DIRECTORY}/SOURCE_DOCUMENTS"

PERSIST_DIRECTORY = f"{ROOT_DIRECTORY}/DB"

MODELS_PATH = "./models"

# Can be changed to a specific number
INGEST_THREADS = os.cpu_count() or 8

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
    anonymized_telemetry=False,
    is_persistent=True,
)

# Context Window and Max New Tokens
CONTEXT_WINDOW_SIZE = 4096
MAX_NEW_TOKENS = CONTEXT_WINDOW_SIZE  # int(CONTEXT_WINDOW_SIZE/4)

#### If you get a "not enough space in the buffer" error, you should reduce the values below, start with half of the original values and keep halving the value until the error stops appearing

N_GPU_LAYERS = 100  # Llama-2-70B has 83 layers
N_BATCH = 512

### From experimenting with the Llama-2-7B-Chat-GGML model on 8GB VRAM, these values work:
# N_GPU_LAYERS = 20
# N_BATCH = 512


# https://python.langchain.com/en/latest/_modules/langchain/document_loaders/excel.html#UnstructuredExcelLoader
DOCUMENT_MAP = {
    ".txt": TextLoader,
    ".md": TextLoader,
    ".py": TextLoader,
    ".pdf": PDFMinerLoader,
    #".pdf": UnstructuredFileLoader,
    ".csv": CSVLoader,
    ".xls": UnstructuredExcelLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".docx": Docx2txtLoader,
    ".doc": Docx2txtLoader,
}

# Default Instructor Model
EMBEDDING_MODEL_NAME = "hkunlp/instructor-large"  # Uses 1.5 GB of VRAM (High Accuracy with lower VRAM usage)

#### SELECT AN OPEN SOURCE LLM (LARGE LANGUAGE MODEL)
# Select the Model ID and model_basename
# load the LLM for generating Natural Language responses

#### GPU VRAM Memory required for LLM Models (ONLY) by Billion Parameter value (B Model)
#### Does not include VRAM used by Embedding Models - which use an additional 2GB-7GB of VRAM depending on the model.
####
#### (B Model)   (float32)    (float16)    (GPTQ 8bit)         (GPTQ 4bit)
####    7b         28 GB        14 GB       7 GB - 9 GB        3.5 GB - 5 GB
####    13b        52 GB        26 GB       13 GB - 15 GB      6.5 GB - 8 GB
####    32b        130 GB       65 GB       32.5 GB - 35 GB    16.25 GB - 19 GB
####    65b        260.8 GB     130.4 GB    65.2 GB - 67 GB    32.6 GB -  - 35 GB


#************************************************DEFAULT MODEL

#The No 1 - the best for retrieving information
MODEL_ID = "TheBloke/Nous-Hermes-Llama-2-7B-GPTQ"
MODEL_BASENAME = "model.safetensors"

#************************************************DEFAULT MODEL