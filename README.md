# CoRa

Notes on replicating results from Weber and Whelan (https://www.biorxiv.org/content/early/2018/08/03/378893) using BppSuite (https://github.com/BioPP/bppsuite; Gu&#233;guen et al., 2013).

The folder ./scripts/run_models/ contains configuration information and scripts.

## Comparison of results

Alignments from large-Ne taxa (blue) disfavour radical nonsynonymous substitutions, while small-Ne taxa (red) show a less pronounced pattern for both comparisons.

<img src="https://github.com/claudia-c-weber/CoRa/blob/master/Co_vs_Ra_bppml_mm.png" alt="" width=800>

Statistical support for CoRa over M0, as indicated by values falling above the vertical black line, is consistently stronger when Ne is large.

<img src="https://github.com/claudia-c-weber/CoRa/blob/master/LRTs.png" alt="" width=800>

Minor discrepancies in estimates may be driven by slight differences in optimisation, gap handling, lower bounds on parameter estimates and starting trees.
