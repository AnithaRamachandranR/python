from __future__ import print_function
from pkg_resources import resource_string
from jenkinsapi.jenkins import Jenkins

jenkins = Jenkins('http://localhost:8080')
job_name = 'foo_job2'
xml = resource_string('examples', 'addjob.xml')

print(xml)

job = jenkins.create_job(jobname=job_name, xml=xml)

# Get job from Jenkins by job name
my_job = jenkins[job_name]
print(my_job)
