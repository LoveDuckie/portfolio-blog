#!/bin/bash
<<EOF

   Portfolio Blog \ Publish \ Blogs

   Publish all blogs that are found under "/blogs/" in the root of the repository.

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath $0))}
export SHARED_SCRIPTS_PATH=${SHARED_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/scripts)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename $0)}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
source "$SHARED_SCRIPTS_PATH/shared.sh"
write_header

if ! is_pyenv_available; then
   write_error "publish" "pyenv is not installed or available from the command-line. unable to continue."
   exit 2
fi

if ! is_python_available; then
   write_error "publish" "python is not installed or available. unable to continue."
   exit 1
fi

is_valid_blog() {
   if [ ! -z $1 ]; then
      write_error "publish" "the blog slug was not specified as the parameter."
      exit 1
   fi
   return 0
}

usage() {
   write_info "publish" "usage - publish"
   write_info "publish" "./publish.sh [-b <blog slug name>] [-s <blog collection name>]"
   exit 0
}

while getopts ':b:h?' opt; do
   case $opt in
   b)
      BLOG_SLUG_NAME=$OPTARG
      write_warning "publish" "publishing \"$BLOG_SLUG_NAME\""
      ;;
   s)
      BLOG_collection_SLUG_NAME=$OPTARG
      write_warning "publish" "publishing \"$BLOG_SLUG_NAME\""
      ;;
   h | ?)
      usage
      ;;
   :)
      write_error "publish" "\"-${OPTARG}\" requires an argument"
      usage
      ;;
   *)
      write_error "publish" "\"-${OPTARG}\" was not recongised."
      usage
      ;;
   esac
done
