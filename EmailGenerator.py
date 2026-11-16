
import re
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "sample_input.txt"
OUTPUT_FILE = Path(__file__).resolve().parent / "extracted_emails.txt"

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(text):
    emails = re.findall(EMAIL_PATTERN, text)
    unique_emails = list(dict.fromkeys(emails))
    return unique_emails


def main():
    print("=" * 35)
    print("       EMAIL EXTRACTOR")
    print("=" * 35)

    if not INPUT_FILE.exists():
        sample_text = """
        Contact us at support@gmail.com
        For help: admin@yahoo.com
        Business: contact@example.com
        Another email: student@gmail.com
        """

        INPUT_FILE.write_text(sample_text, encoding="utf-8")
        print("Sample input file created successfully!")

    try:
        text = INPUT_FILE.read_text(encoding="utf-8")

        emails = extract_emails(text)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")

        print("\nExtracted Email Addresses:")

        for email in emails:
            print(email)

        print("\nTotal unique emails found:", len(emails))
        print("Results saved in extracted_emails.txt")

    except OSError as error:
        print("File Error:", error)


if __name__ == "__main__":
    main()
