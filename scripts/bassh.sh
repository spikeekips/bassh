_bassh_bash_complete ()
{
  local curr_arg;

  #echo '.....................'
  #echo aa ':' "(${COMP_WORDS[*]})"
  #curr_arg=${COMP_WORDS[COMP_CWORD]}
  #echo b ':' "|${curr_arg}|"
  #echo '.....................'

  prog=${COMP_WORDS[0]}

  COMPREPLY=($($prog --bassh-comp -- "${COMP_WORDS[*]}" ))
}

complete -F _bassh_bash_complete bassh.py


