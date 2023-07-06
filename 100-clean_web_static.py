def do_clean(number=0):
  """Deletes out-of-date archives.
  number is the number of the archives, including the most recent, to keep. If
  number is 0 or 1, keep only the most recent version of your archive. if
  number is 2, keep the most recent, and second most recent versions of your
  archive. etc.
  Args:
    number: The number of archives to keep.
  """
  # Delete all unnecessary archives (all archives minus the number to keep) in the
  # versions folder.
  with cd('versions'):
    for archive in listdir('.'):
      if archive.endswith('.tar.gz'):
        if int(archive.split('-')[-1][:-7]) < number:
          delete(archive)
  # Delete all unnecessary archives (all archives minus the number to keep) in the
  # /data/web_static/releases folder of both of your web servers.
  for host in ['web1', 'web2']:
    with cd('/data/web_static/releases'):
      for archive in listdir('.'):
        if archive.endswith('.tar.gz'):
          if int(archive.split('-')[-1][:-7]) < number:
            sudo('rm -f {}'.format(archive))
