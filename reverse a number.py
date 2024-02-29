def print_words_starting_with_letter(letter):
    """
    Function to print words from each category that start with the specified letter.
    """
    letter = letter.upper()

    words = {
        'name': ['Alexander','Bharath','Charan','David','Emily','Frank','Grace','Henry','Isabella','James','Krishna','Liam','Mia','Noah','Olivia','Patrick','Quinn','Rachel','Samuel','Taylor','Ursula','Victor','Willow','Xavier','Yasmine','Zachary'],
        'place': ['Afghanistan','Brazil','Canada','Denmark','Egypt','France','Germany','Hungary','India','Japan','Kenya','Lebanon','Mexico','Norway','Oman','Peru','Qatar','Russia','Spain','Turkey','United States','Vietnam','Wales','Xax','Yemen','Zambia'],
        'thing': ['Apple','Book','Chair','Door','Egg','Fork','Globe','Hat','Ice cream','Juice box','Key','Lamp','Mirror','Notebook','Orange','Pencil','Quilt','Radio','Shoes','Table','Umbrella','Violin','Watch','Xylophone','Yarn','Zipper'],
        'animal': ['Armadillo','Bat','Cheetah','Dolphin','Elephant','Fox','Gorilla','Hawk','Iguana','Jellyfish','Koala','Lion','Monkey','Newt','Ostrich','Penguin','Quokka','Rabbit','Sloth','Tiger','Uakari','Vulture','Walrus','X-ray Tetra','Yak','Zebra']
    }

    print(f"Words starting with '{letter}':")
    for category, category_words in words.items():
        matching_words = [word for word in category_words if word.startswith(letter)]
        if matching_words:
            print(f"{category.capitalize()}: {', '.join(matching_words)}")
        else:
            print(f"{category.capitalize()}: No matching word")

if __name__ == "__main__":
    input_letter = input("Enter a letter: ")
    print_words_starting_with_letter(input_letter)
