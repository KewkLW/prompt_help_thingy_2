import streamlit as st
import os

def run_append_script():

    def generate_text(main_text, additional_text, prefix, suffix, output_dir):
        main_text = [mt for mt in main_text.split('\n') if mt.strip() != ''] if main_text else ['']
        additional_text = [at for at in additional_text.split('\n') if at.strip() != ''] if additional_text else ['']
        prefix = [p for p in prefix.split('\n') if p.strip() != ''] if prefix else ['']
        suffix = [s for s in suffix.split('\n') if s.strip() != ''] if suffix else ['']

        output_file_path = os.path.join(output_dir, 'output.txt')
        with open(output_file_path, 'w') as f:
            for mt in main_text:
                for at in additional_text:
                    for p in prefix:
                        for s in suffix:
                            line = ' '.join(filter(None, [p, mt, at, s]))
                            if line.strip():
                                f.write(line + '\n')
                        f.write('\n')

        return f"Text file has been written successfully to {output_file_path}."

    st.header("Append Script")
        
    # Inputs
    prefix = st.text_area("Prefix")
    main_text = st.text_area("Main Text") 
    additional_text = st.text_area("Additional Text")
    suffix = st.text_area("Suffix")
    output_dir = st.text_input("Output Directory")

    # Button to run the function
    if st.button("Generate Text"):
        result = generate_text(main_text, additional_text, prefix, suffix, output_dir)
        st.write(result)

run_append_script()