# Real World Graph Pre-Processing

This folder contains real-world graph pre-processing programs for two networks: "AS" and "eu-core." The respective GML files, such as `as.gml` and `eu-core.gml`, store information in GML format for these networks.

## Files

- **AS Network:**
  - `as.gml`: GML file storing information for the AS network.
  - `GML_2_NetworkX & Test.ipynb`: Jupyter notebook to extract network information.
    - Outputs:
      - `as.edgelist`: Edge list extracted from the AS network.
      - `as_pre.membership`: Community membership information before processing.
      - `as.membership`: Community membership information after processing.

- **EU-Core Network:**
- `EU-Core.gml`: GML file storing information for the EU-Core  network.
  - `GML_2_NetworkX & Test.ipynb`: Jupyter notebook to extract network information.
    - Outputs:
      - `eu-core.edgelist`: Edge list extracted from the EU-Core  network.
      - `eu-core_pre.membership`: Community membership information before processing.
      - `eu-core.membership`: Community membership information after processing.

## Usage

1. Open the `GML_2_NetworkX & Test.ipynb` notebook for detailed instructions and comments.
2. Run the notebook to extract the required network information.

## Notes

- Detailed comments within the notebook provide insights into the extraction process and the generated output files.

Feel free to explore and utilize the pre-processed data for further analysis or integration into your research.

For any questions or issues, please refer to the documentation or contact zfwei11@gmail.com.
