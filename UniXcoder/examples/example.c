static int edit (char *file_name) {
  char    buf[1024];
  char    *editor;

  if (!(editor = getenv ("EDITOR")))
    editor = DEFAULT_EDITOR;
  if (!file_name)
    file_name = "";
  (void) snprintf(buf, <mask0>, "%s %s", editor, file_name);
}

