_bassh_bash_complete ()
{
  local curr_arg;

  prog=${COMP_WORDS[0]}

  COMPREPLY=($($prog --bassh-comp -- "${COMP_WORDS[*]}" ))
}

complete -F _bassh_bash_complete bassh


