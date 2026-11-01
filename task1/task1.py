def total_salary(path):
    """Calculate the total and average salaries from a file."""
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                _, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        average = total / count if count else 0
        return total, average

    except FileNotFoundError:
        print(f"File not found: {path}")
    except (ValueError, UnicodeError):
        print(f"Invalid data in file: {path}")
    except OSError as error:
        print(f"Error reading file: {error}")

    return 0, 0

total, average = total_salary("salary.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:g}")