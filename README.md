# isp-ticketingSystem
**isp-ticketingSystem** is a simple web based open source support ticketing system written in Python
using the flask web framework. It seamlessly integrates inquiries created via web-based forms into a
simple easy-to-use multi-user web interface. Manage, organize and review all your support requests
and responses in one place while providing your customers with accountability and
responsiveness they deserve.


## How isp-ticketingSystem works for you
  1. Users create tickets via your website
  2. Incoming tickets are saved and assigned to admins
  3. Agents help your users resolve their issues

isp-ticketingSystem is an attractive alternative to higher-cost and complex customer support systems;
simple, lightweight, reliable, open source, web-based and easy to setup and use.
The best part is, it's completely free.


## Requirements
    * Python
    * Flask version 2.1.2
    * SQLAlchemy version 1.4.36


## Deployment
isp-ticketingSystem now supports bleeding-edge installations.
The easiest way to install the software and track updates is to clone the public repository.
Create a folder on you web server (using whatever method makes sense for you) and cd into it.
Then clone the repository (the folder must be empty!):
    git clone https://github.com/mansijmaharzn/isp-ticketingSystem

And deploy the code into somewhere in your server's www root folder, for
instance

    cd isp-ticketingSystem
    python main.py


## Upgrading
isp-ticketingSystem supports upgrading from current and later versions in future.
As with any upgrade, strongly consider a backup of your attachment files, database, and
isp-ticketingSystem codebase before embarking on an upgrade.


### Upgrading from versions
**WARNING**: If you are upgrading isp-ticketingSystem, please ensure that all
    your files in your upload folder are both readable and writable.
    Unreadable files will not be migrated to the database during
    the upgrade and will be effectively lost.


## Help
E-mail Us if you'd like professional help managing your isp-ticketingSystem installation.


## License
isp-ticketingSystem is released under the GPL2 license. See the included LICENSE.txt
file for the gory details of the General Public License.
Which is not there yet hehe! (will add in future)