def find_highest_gwa():
    filename = "students_name_and_gwa.txt"

    try:
        with open(filename, "r") as file:
            max_gwa = None
            max_student = ""

            for line_num, line in enumerate(file, 1):
                parts = line.strip().split()
                if len(parts) < 2:
                    continue

                student_name = ' '.join(parts[:-1])
                try:
                    gwa = float(parts[-1])
                except ValueError:
                    continue

                if max_gwa is None or gwa < max_gwa:  # lowest GWA = best
                    max_gwa = gwa
                    max_student = student_name

            if max_student:
                print(f"Student with highest GWA:")
                print(f"Name: {max_student}")
                print(f"GWA: {max_gwa:.2f}")
            else:
                print("No valid student data found.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


if __name__ == "__main__":
    find_highest_gwa()
