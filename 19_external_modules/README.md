Virtual Environments & Package Management
As you start working on more Python projects, you'll likely use different versions of libraries. Virtual environments help isolate project dependencies, preventing conflicts between different projects.

Virtual Environments:

A virtual environment is a self-contained directory that contains its own Python interpreter and libraries. This means that libraries installed in one virtual environment won't interfere with libraries in another.

Creating a virtual environment (using venv - recommended):

python3 -m venv my_env  # Creates a virtual environment named "my_env"

Activating the virtual environment:

Windows: my_env\Scripts\activate
macOS/Linux: source my_env/bin/activate
Once activated, you'll see the virtual environment's name in your terminal prompt (e.g., (my_env)).

Package Management (using pip):

pip is Python's package installer. It's used to install, upgrade, and manage external libraries.

Installing a package:

pip install requests  # Installs the "requests" library
pip install numpy==1.20.0 # Installs a specific version

Listing installed packages:

pip list

Upgrading a package:

pip install --upgrade requests

Uninstalling a package:

pip uninstall requests

Generating a requirements file:

A requirements.txt file lists all the packages your project depends on. This makes it easy to recreate the environment on another machine.

pip freeze > requirements.txt  # Creates the requirements file
pip install -r requirements.txt  # Installs packages from the file

Deactivating the virtual environment:

deactivate

---

Troubleshooting: PowerShell Execution Policy Error

Error:
PS C:\Users\Rupayan\Desktop\Python Course\19_external_modules> .\env1\Scripts\activate .\env1\Scripts\activate : File C:\Users\Rupayan\Desktop\Python Course\19_external_modules\env1\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170. At line:1 char:1 + .\env1\Scripts\activate + ~~~~~~~~~~~~~~~~~~~~~~~ + CategoryInfo : SecurityError: (:) [], PSSecurityException + FullyQualifiedErrorId : UnauthorizedAccess

Solution (Recommended & Safe):

Allow scripts only for your user account.

Step 1: Open PowerShell as your normal user
(No admin needed)

Step 2: Run this command
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Step 3: Press Y and Enter

Step 4: Activate your venv again
.\env1\Scripts\activate

You should now see:
(env1) PS C:\Users\Rupayan\Desktop\Python Course\19_external_modules>
