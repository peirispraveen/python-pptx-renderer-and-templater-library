import os
from pptx_templater.core import convert


def test_conversion():
    currpwd = os.path.dirname(os.path.abspath(__file__))
    srcpath = f'{currpwd}/input_dir/File Format for Control Union.pptx'
    destpath = f'{currpwd}/output_dir/updated.pptx'

    data = {
        "deforestation_text": "Deforestation risk is low",
        "encroachment_text1": "Encroachment risk is low ",
        "deforestation_text2": "Deforestation risk is low",
        "encroachment_text2": "Encroachment risk is low ",
        "deforestation_text3": "Deforestation risk is low",
        "encroachment_text3": "Encroachment risk is low ",
        "deforestation_text4": "Deforestation risk is low",
        "encroachment_text4": "Encroachment risk is low ",
        "total_area_val": "0.12 ha",
        "potec_val": "0.00 ha",
        "def_val": "0.00ha",
        "eligible_area_val": "0.12ha",
        "tec_val": "20M"
    }

    # Since there's only one slide, map all placeholders on that single slide
    j = {
        'slides': [
            {
                'layoutSlideNum': 0,  # Assuming 0 is the layout number for the single slide
                'text': {
                    'deforestation_text': data['deforestation_text'],
                    'encroachment_text1': data['encroachment_text1'],
                    'deforestation_text2': data['deforestation_text2'],
                    'encroachment_text2': data['encroachment_text2'],
                    'deforestation_text3': data['deforestation_text3'],
                    'encroachment_text3': data['encroachment_text3'],
                    'deforestation_text4': data['deforestation_text4'],
                    'encroachment_text4': data['encroachment_text4'],
                    'total_area_val': data['total_area_val'],
                    'potec_val': data['potec_val'],
                    'def_val': data['def_val'],
                    'eligible_area_val': data['eligible_area_val'],
                    'tec_val': data['tec_val']
                }
            }
        ]
    }

    convert(srcpath, destpath, j)


if __name__ == "__main__":
    test_conversion()
