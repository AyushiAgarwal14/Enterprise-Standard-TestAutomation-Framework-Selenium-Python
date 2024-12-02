import getpass
import os
import requests
import json
import datetime


class ActiveUsers:

    @staticmethod
    def get_username():
        print("***Privacy Disclaimer: During run, we collect user details such us User's Name, packagename, "
              "packageversion and execution details to enhance your experience and "
              "assure you that your information is handled with utmost care.Please reach out to FE Team for any "
              "queries ***")
        username = getpass.getuser()
        return username

    @staticmethod
    def get_project_name():
        project_name = input("Please Provide us the project name:")
        return project_name

    @staticmethod
    def get_project_name_azure():
        if 'TF_BUILD' in os.environ:
            return "AzurePipeline_Project"
        elif 'GITHUB_ACTIONS' in os.environ:
            return "GitHubActions_Project"
        else:
            project_name = ActiveUsers.get_project_name()
            return project_name

    @staticmethod
    def collect_user_details(package_name, package_version):
        username = ActiveUsers.get_username()
        if package_version == 'unknown':
            package_version = "Script execution from Inner source/Admin"
        ActiveUsers.insert_value(username, package_name, package_version)

    @staticmethod
    def insert_value(username, package_name, package_version):

        # Get project name from the GET request
        # url = "https://qadashbaord.azurewebsites.net/"
        get_url = "https://feactiveuserdetails.azurewebsites.net/get_project/"
        post_url = "https://feactiveuserdetails.azurewebsites.net/update_project/"
        headers = {"Content-Type": "application/json"}
        params = {
            "user_name": username,
            "package_name": package_name,
            "package_version": package_version
        }
        # print(get_url, params, headers)
        response = requests.get(get_url, params=params, headers=headers)
        # response_data = response.json()
        if response.status_code == 200 or response.status_code == 404:
            try:
                response_data = response.json()
                # Check if the response contains valid JSON
                if isinstance(response_data, dict):
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    project_name = response_data.get("project_name")
                    # If project name is not available, prompt the user to enter it
                    if not project_name:
                        project_name = ActiveUsers.get_project_name_azure()
                    # Add project name to the data for the POST request
                    data = {
                        "user_name": username,
                        "package_name": package_name,
                        "package_version": package_version,
                        "Project_name": project_name,
                        "Last_execution_time": current_time
                    }
                    # Make the POST request
                    response = requests.post(post_url, json=data, headers=headers)

                    if response.status_code == 200:
                        # print("Updated the user details to the database")
                        pass
                    elif response.status_code == 500:
                        # Internal server error
                        print("Internal server error")
                    else:
                        print("Post request failed.", response.status_code)
                else:
                    print("Invalid JSON response.")
            except json.JSONDecodeError as e:
                print("Error decoding JSON response:", str(e))
        else:
            print("GET request failed.")

# if __name__ == "__main__":
#     ActiveUsers.collect_user_details("Shell_FE_Selenium_Core", "2.0.0b2")
