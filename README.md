ndb-backup
----------

This tool allows you to easily backup your NDB data to an excel sheet,
or rebuild an NDB datastore from a previous backup file.

The actual relevant files are /handlers/ndbBackup.py and /handlers/ndbRecover.py
Everything else serves as a workspace for development.

This tool utilizes a map of the different models you use throughout your application.
You can find an example map in /models/models_map.py

Basically the necessary map is an array of dictionaries, where each dictionary represents a class and holds a general class name, a specific class name ('repr') - equivalent to __class__.__name__, and two extra dictionaries to hold properties and references.

Using this map, the tool iterates over all datastore entities and saves the specified fields (from the map) in an excel sheet, where each model class gets its own sheet. So in the end you have a sheet with all User's, a sheet with all Addresses, etc, including all the one-to-one, one-to-many references, etc.

The recovery process works similarly, using the models map to restore the datastore from the saved excel file.