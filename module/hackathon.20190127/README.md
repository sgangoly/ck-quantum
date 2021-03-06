# Paris Quantum Computing Hackathon, 27 January 2019

* [Meetup](https://www.meetup.com/Paris-Quantum-Computing-Technologies/events/256367871) (**upcoming!**)
* Slides (link to Riverlane's slides) - Dropbox shared for reading?
* Location of Riverlane's "paris" repository with pickled problems and solution code examples - Dropbox shared for reading?

## Getting started (ideally done BEFORE the day of the Hackathon to save the precious competition time - feedback welcome)

1. Install python3
1. Install qiskit and its dependencies (reinstall marshmallow 2.15.0 on OSX to avoid being drowned in warnings)
1. A quick test to see that qiskit simulator works
1. Install CK

## The hackathon workflow

### Running evaluate.py (insert multiple examples)

...

...

## Using CK (Collective Knowledge framework) for viewing and sharing the solutions

The main type of object that CK works with is called a "CK entry".
A "CK entry" is a directory with meta-data, optional data and optional code.

You will use CK tools to:
1. convert your solutions into CK experiment entries
1. look at your own entries using "CK Dashboard" in local mode
1. upload your CK experiment entries to the shared server and
1. view everybody's results using a shared CK dashboard on the server.

### Storing an experiment entry locally

Each run of evaluate.py leaves a .JSON output file in the current directory.
In order to be counted as a solution, viewed in context of others and uploaded
it will have to be first "stored" as a CK entry:

```
$ ck store_experiment qml --json_file=<json_file_name> [--team=<schroedinger-cat-herders>]
```

A CK experiment entry is stored together with the team name.
You can either supply it from the command line or enter it interactively at a prompt.

### Viewing the locally stored experiments

To see the local experimental entries on a diagram:
```
$ ck display dashboard --scenario=hackathon.20190127
```
This command will open a browser page and will turn itself into a server to that page.
You can leave this server command running in its own terminal and open a new one.
Or you can kill it when the page loads and reclaim the terminal - your choice.

### Uploading the results to the common shared server

In order for your solution to count in the competition, you will have to upload
your best results to the server:
```
$ ck upload qml [ <experiment entries> ]
```
If you don't specify the entries to upload, this command will prompt you to choose one from a list.
Please note that your competition points will depend on who uploads their solution to the server faster
(the uploading timestamp counts, not the running timestamp). So upload as soon as you are ready.

### Viewing the remotely shared experiments

Visit [Shared dashboard page](http://cknowledge.org/dashboard/hackathon.20190127) (**upcoming!**)
