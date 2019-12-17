
# pom.xml should have <packaging>war</packaging> configured
mvn install && 

# copy to remote server on specific tomcart folder
scp {project /target folder}/yourJavaApp-0.0.1-SNAPSHOT.war sshUser@1.ip.1.1:/root/apache-tomcat-9.0.30/webapps/ROOT.war &&

# restart.sh just calls shutdown.sh and startup.sh from tomcat bin folder  
ssh sshUser@1.ip.1.1 bash restart.sh

