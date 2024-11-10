class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def __str__(self):
        # Määritellään authors_str, jotta se voi olla helposti tulostettavissa
        authors_str = "\n- ".join(self.authors) if self.authors else "-"

        # Listataan riippuvuudet ja kehityksen aikaiset riippuvuudet allekkain
        dependencies_str = "\n- ".join(self.dependencies) if self.dependencies else "-"
        dev_dependencies_str = "\n- ".join(self.dev_dependencies) if self.dev_dependencies else "-"

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\nAuthors:\n- {authors_str}"
            f"\nDependencies:\n{dependencies_str}"
            f"\nDevelopment dependencies:\n{dev_dependencies_str}"
        )
