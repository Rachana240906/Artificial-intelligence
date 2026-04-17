# Graph representation (adjacency list)
graph = {
    "Kutch": ["Banaskantha", "Rajkot", "Surendranagar", "Patan"],
    "Banaskantha": ["Mehsana", "Patan", "Sabarkantha", "Kutch"],
    "Patan": ["Banaskantha", "Mehsana", "Surendranagar", "Ahmedabad", "Kutch"],
    "Mehsana": ["Patan", "Sabarkantha", "Ahmedabad", "Banaskantha", "Gandhinagar", "Surendranagar"],
    "Sabarkantha": ["Banaskantha", "Mehsana", "Gandhinagar", "Kheda", "Panchmahal"],
    "Gandhinagar": ["Sabarkantha", "Ahmedabad", "Kheda", "Mehsana"],
    "Ahmedabad": ["Mehsana", "Gandhinagar", "Kheda", "Anand", "Surendranagar", "Bhavnagar"],
    "Kheda": ["Gandhinagar", "Ahmedabad", "Anand", "Sabarkantha", "Panchmahal", "Vadodara"],
    "Anand": ["Ahmedabad", "Kheda", "Vadodara"],
    "Vadodara": ["Anand", "Kheda", "Panchmahal", "Dahod", "Bharuch", "Narmada"],
    "Panchmahal": ["Kheda", "Sabarkantha", "Vadodara", "Dahod"],
    "Dahod": ["Panchmahal", "Vadodara"],
    "Surendranagar": ["Ahmedabad", "Bhavnagar", "Rajkot", "Patan", "Kutch"],
    "Rajkot": ["Surendranagar", "Jamnagar", "Junagadh", "Bhavnagar", "Amreli", "Porbandar", "Kutch"],
    "Jamnagar": ["Rajkot", "Porbandar"],
    "Porbandar": ["Jamnagar", "Junagadh", "Rajkot"],
    "Junagadh": ["Rajkot", "Porbandar", "Amreli", "Jamnagar"],
    "Amreli": ["Junagadh", "Rajkot", "Bhavnagar"],
    "Bhavnagar": ["Amreli", "Rajkot", "Surendranagar", "Ahmedabad"],
    "Bharuch": ["Vadodara", "Narmada", "Surat"],
    "Narmada": ["Vadodara", "Bharuch", "Surat"],
    "Surat": ["Bharuch", "Narmada", "Navsari", "Dang"],
    "Navsari": ["Surat", "Valsad", "Dang"],
    "Valsad": ["Navsari"],
    "Dang": ["Navsari", "Surat"]
}


colors = ["Red", "Blue", "Green", "Yellow"]

def is_safe(node, color, question):
    for neighbour in graph[node]:
        if neighbour in question and question[neighbour] == color:
            return False
    return True


def solve(question):
    if len(question) == len(graph):
        return question

    # Select unassigned node
    node = [n for n in graph if n not in question][0]

    for color in colors:
        if is_safe(node, color, question):
            question[node] = color
            result = solve(question)
            if result:
                return result
            del question[node]

    return None

# Run CSP
solution = solve({})

# Print result
if solution:
    for district, color in solution.items():
        print(f"{district}: {color}")
else:
    print("No solution found")
