import argparse

import lancedb
from sentence_transformers import SentenceTransformer

db = lancedb.connect("./.lancedb")

embed_models = {
    "Alibaba-NLP/gte-large-en-v1.5": SentenceTransformer(
        "Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True
    )
}

lookup_dataset_names = db.table_names()

current_embed_model_name: str = list(embed_models.keys())[0]
current_lookup_dataset_name: str = lookup_dataset_names[0]

while True:
    main_menu_choice: int = int(
        input(
            f"""
1. Change embedding model (currently '{current_embed_model_name}')
2. Choose lookup dataset (currently '{current_lookup_dataset_name}')
3. Query dataset
4. Exit
        """
        )
    )
    if main_menu_choice == 4:
        exit()
#     model_choice_idx = int(
#         input(
#             f"""
# \033[H\033[J
# Please choose an embedding model:
# {"\n\t".join( [f"{idx}. {model_name}" for idx, model_name in enumerate(embed_models.keys())])}
#         """
#         )
#     )
#     embed_model = embed_models[list(embed_models.keys())[model_choice_idx]]


# table = db.open_table("chunk_by_fixed_size-chunk_nchar500-overlap_nchar100")
# encoded_query = embed_model.encode(args.query)
#
# for search_rank, search_result in enumerate(
#     table.search(encoded_query).limit(5).to_list(), start=1
# ):
#     print(f"-- Result Rank {search_rank} --")
#     for key in (
#         "source_doc",
#         "chunk_num",
#         "chung_alg",
#         "chunk_alg_params",
#         "char_start_index",
#         "char_end_index",
#         "text",
#     ):
#         print("\t", key, ": ", search_result[key])
#     print()
