from pptx_renderer import PPTXRenderer


def input_data_and_save_pptx(template_path, output_path, data):
    """
    Inputs data into placeholders in a PowerPoint template and saves it as a PPTX.

    Args:
        template_path: Path to the PowerPoint template file.
        output_path: Path to save the output PPTX file.
        data: Dictionary containing data to be inserted into placeholders.
    """
    # Initialize the PPTXRenderer with the template path
    renderer = PPTXRenderer(template_path)

    # Render the PowerPoint with the data
    renderer.render(output_path, data)


# Example usage
template_path = "input_dir/File Format for Control Union.pptx"
output_path = "output_dir/CU_report_from_pptx_renderer.pptx"
data = {
    "deforestation_text1": "Deforestation risk is low",
    "encroachment_text1": "Encroachment risk is low",
    "deforestation_text2": "Deforestation risk is low",
    "encroachment_text2": "Encroachment risk is low",
    "deforestation_text3": "Deforestation risk is low",
    "encroachment_text3": "Encroachment risk is low",
    "deforestation_text4": "Deforestation risk is low",
    "encroachment_text4": "Encroachment risk is low",
    "total_area_val": "0.12 ha",
    "potec_val": "0.00 ha",
    "def_val": "0.00ha",
    "eligible_area_val": "0.12ha",
    "tec_val": "20M"
}

# Input the data and save as a PowerPoint file
input_data_and_save_pptx(template_path, output_path, data)
