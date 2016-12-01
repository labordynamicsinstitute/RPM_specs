#!/bin/bash

# this section modifies the preferences for multi-user systems, but only upon first start
JABREF_PREFS=$HOME/.java/.userPrefs/net/sf/jabref/prefs.xml
JABREF_KEY_RSERV=useRemoteServer
JABREF_KEY_SET=setRemoteServer
JABREF_PORT=$(awk -v min=2000 -v max=10000 'BEGIN{srand(); print int(min+rand()*(max-min+1))}')
# we should really check if this is not used somehow...
JABREF_USE_SERVER_DEFAULT=true
JABREF_PREFS_DEFAULT="<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>
<!DOCTYPE map SYSTEM \"http://java.sun.com/dtd/preferences.dtd\">
<map MAP_XML_VERSION=\"1.0\">
  <entry key=\"setRemoteServer\" value=\"true\"/>
  <entry key=\"useRemoteServer\" value=\"$JABREF_USE_SERVER_DEFAULT\"/>
  <entry key=\"remoteServerPort\" value=\"$JABREF_PORT\"/>
 </map>
"

if [[ -f $JABREF_PREFS ]]
then
  # prefs exist, we modify if not modified
  _PREFS_SET=$(grep setRemoteServer $JABREF_PREFS)
  if [[ -z $_PREFS_SET ]]
  then
    # we haven't done this before, so we modify
    # Is there a remote server entry already
    _PORT_SET=$(grep remoteServerPort $JABREF_PREFS)
    if [[ -z $_PORT_SET ]]
    then
      sed -i "s+</map>+  <entry key=\"remoteServerPort\" value=\"$JABREF_PORT\"/>\n</map>+"  $JABREF_PREFS
    else
      # replace any previous Port with the value set above
      sed -i "/remoteServerPort/ { s+value=\"[0-9]*\"+value=\"$JABREF_PORT\"+ }"  $JABREF_PREFS
    fi
    # Is the remote server active
    #_SERVER_SET=$(grep useRemoteServer $JABREF_PREFS)
    #if [[ -z $_SERVER_SET ]]
    #then
    #  sed -i "s+</map>+  <entry key=\"useRemoteServer\" value=\"false\"/>\n</map>+"  $JABREF_PREFS
    #else
    #  # replace any previous Port with the value set above
    #  sed -i "/useRemoteServer/ { s+value=\"true\"+value=\"false\"+ }"  $JABREF_PREFS
    #fi
    # now make a note that we have done this
    sed -i 's+</map>+  <entry key="setRemoteServer" value="true"/>\n</map>+' $JABREF_PREFS
  fi
else
  # prefs don't exist, we initialize
  echo "$JABREF_PREFS_DEFAULT" > $JABREF_PREFS
fi
# this line is added by the spec file, to correspond to the correct binary
#java -jar /usr/share/jabref3/JabRef-3.7.jar &
