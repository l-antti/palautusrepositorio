import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # Tulosta ladattu merkkijono (tiedoston sisältö)
        #print("Tiedoston sisältö (raw TOML):")
        #print(content)

        # Deserialisoi TOML-muotoista dataa
        toml_data = toml.loads(content)
        #print("Deserialisoitu data:\n", toml_data)

         # Hae projektin tiedot
        project_name = toml_data["tool"]["poetry"]["name"]
        project_description = toml_data["tool"]["poetry"]["description"]
        project_license = toml_data["tool"]["poetry"]["license"]
        project_authors = toml_data["tool"]["poetry"]["authors"]

        # Hae riippuvuudet oikeista osioista
        dependencies = list(toml_data["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(toml_data["tool"]["poetry"]["group"].get("dev", {}).get("dependencies", {}).keys())


         # Luo Project-olio
        project = Project(
            project_name,
            project_description,
            dependencies,
            dev_dependencies,
            project_license,
            project_authors
        )


        return project
