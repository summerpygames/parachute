#! /usr/bin/env python
"""Script to build a skeleton Pygame wrapper"""
import os, sys, shutil
DEFAULT_SERVICE_PREFIX = 'org.laptop.community.'
def create( name, title=None, mainloop='run', service=None ):
    """Create new activity directory for given name"""
    if not name:
        raise ValueError( """Need a non-null name""" )
    if not title:
        title = name
    newName = '%s.activity'%(name,)
    if os.path.exists( newName ):
        raise OSError( """%s already exists, cannot create"""%(newName,))
    
    activityDirectory = '%s.activity'%(name,)
    shutil.copytree( 'skel.activity',activityDirectory )

    if service is None:
        service = DEFAULT_SERVICE_PREFIX + name 
    
    namespace = {
        'name': name,
        'title': title,
        'mainloop': mainloop,
        'service': service,
    }
    substitute( newName, namespace )
    
    # now drop in a link to olpcgames...
    gamespath = os.path.join( '..', 'olpcgames' )
    if os.path.isdir( gamespath ):
        os.symlink( os.path.join( '..', gamespath), os.path.join( activityDirectory, 'olpcgames')  )


def substitute( directory, namespace ):
    """Substitute contents of all files with namespace values"""
    for filename in os.listdir( directory ):
        filename = os.path.join( directory, filename )
        if os.path.isfile( filename ):
            previousContent = open( filename ).read()
            try:
                content =  previousContent % namespace
            except KeyError, err:
                err.args += (filename,)
                raise 
            else:
                if content != previousContent:
                    open( filename,'w').write( content )
        elif os.path.isdir( filename ) and os.path.basename( filename ) != 'olpcgames':
            substitute( filename, namespace )

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option(
        "-n", "--name", dest="name", 
        help="Specify simple name of the project (filename)"
    )
    parser.add_option(
        "-t", "--title", dest="title", 
        help="Specify human-readable name of the project (window/icon title)" 
    )
    parser.add_option(
        "-m", "--mainloop", dest='mainloop', default="run",
        help="Mainloop module and function as package.module:function string",
    )
    parser.add_option(
        "-s", "--service", dest="service",default=None,
        help="DBUS service name for the activity, if not provided, will be the name with a prefix",
    )
    (options, args) = parser.parse_args()
    name,title = options.name,options.title
    if args:
        name = args[0]
        if len(args) > 1:
            title = args[1]
    if name:
        create( 
            name = name,
            title = title,
            mainloop = options.mainloop,
            service = options.service,
        )
    else:
        parser.print_help()
    
