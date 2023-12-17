import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    # change handler name
    handlers=[logging.FileHandler("/tmp/xml-json-processor.log"), logging.StreamHandler()],
)

LOGGER = logging.getLogger(__name__)
