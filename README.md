# Git Production Branching Workflow

## Project Overview

This project demonstrates a production-style Git branching strategy using
GitHub pull requests (PRs).

The objective is to practise how developers collaborate, integrate features,
promote code across environments, handle bugs, and synchronize fixes between
branches.

## Branching Strategy

The repository uses the following long-lived branches:

| Branch | Purpose |
|---|---|
| dev | Development and feature integration |
| qa | Quality assurance and testing |
| ppd | Pre-production validation |
| prod | Production-ready code |

Feature and bugfix branches are created separately to isolate individual
changes.

## Branch Workflow

The normal feature promotion workflow is:

1. Create a feature branch from dev.
2. Implement the required change.
3. Commit and push the feature branch.
4. Create a pull request into dev.
5. Review and merge the pull request.
6. Promote dev to qa through a pull request.
7. Promote qa to ppd through a pull request.
8. Promote ppd to prod through a pull request.

### Workflow Diagram

```text
feature/add-task --------\
                          \
                           > DEV
                          /   |
feature/display-tasks ---/    |
                               v
                              QA
                               |
                               v
                              PPD
                               |
                               v
                              PROD
                               |
                               | Back-merge
                               v
                              DEV
