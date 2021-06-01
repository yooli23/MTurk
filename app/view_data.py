from database import view


# Example data retrieval
def main():

    data = view.all()

    for hit in data:
        if hit.complete:
            print("Info:", hit.info)
            print("Dialog:", hit.dialog)
            print("Forms:", hit.forms)     


if __name__ == '__main__':
    main()