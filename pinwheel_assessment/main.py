from Providers.irs_form_processor import IRSFormProcessor


if __name__ == "__main__":

    cmd = input(
        "Type 'FORM NAME INFO' to recieve information on form names.\nType "
        "'DOWNLOAD DOCUMENTS' to download pdf files for form names.\nThen "
        "press 'Enter'.\nType 'QUIT' to quit.\n"
    )
    cmd = cmd.strip().lower()
    while cmd != "quit":

        if cmd == "download documents":
            form_name = input("Enter form name: ").split(",")
            range_of_years = input("Enter range of years in YYYY-YYYY format: ").split(
                "-"
            )
            irs_forms_download = IRSFormProcessor(
                form_names=form_name, range_of_years=range_of_years, cmd=cmd
            )

        elif cmd == "form name info":
            tax_form_names_input = input(
                "Input your tax form names seperated by commas: "
            ).split(",")
            irs_form_processor = IRSFormProcessor(
                form_names=tax_form_names_input, cmd=cmd
            )
            irs_form_processor.irs_forms

        cmd = input(
            "Type 'FORM NAME INFO' to recieve information on form "
            "names.\nType 'DOWNLOAD DOCUMENTS' to download pdf files for form "
            "names.\nThen press 'Enter'.\nType 'QUIT' to quit.\n"
        )
        cmd = cmd.strip().lower()

    print("Quitting...")
