def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, person in enumerate(attendees, start=1):
        try:
            name = person.get("name") or "N/A"
            event_title = person.get("event_title") or "N/A"
            event_date = person.get("event_date") or "N/A"
            event_location = person.get("event_location") or "N/A"

            output_text = template
            output_text = output_text.replace("{name}", str(name))
            output_text = output_text.replace("{event_title}", str(event_title))
            output_text = output_text.replace("{event_date}", str(event_date))
            output_text = output_text.replace("{event_location}", str(event_location))

            file_name = f"output_{index}.txt"

            with open(file_name, "w") as file:
                file.write(output_text)

        except Exception as e:
            print(f"Error processing attendee {index}: {e}")
