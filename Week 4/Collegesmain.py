from College import College

def main():
    # create two college objects
    college1 = College("University of South Carolina", "Public", "Columbia", "South Carolina")
    college2 = College("Clemson University", "Public", "Clemson", "South Carolina")

    # print data for college1 to console
    print("COLLEGE DATA")
    print(f"Name:             {college1.name}")
    print(f"Type:             {college1.PublicorPrivate}")
    print(f"Location:         {college1.getLocation()}")

    # print data for college2 to console
    print("\nCOLLEGE DATA")
    print(f"Name:             {college2.name}")
    print(f"Type:             {college2.PublicorPrivate}")
    print(f"Location:         {college2.getLocation()}")

if __name__ == "__main__":
    main()