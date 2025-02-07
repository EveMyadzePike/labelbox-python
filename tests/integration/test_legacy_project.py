import pytest

from labelbox.schema.queue_mode import QueueMode


def test_project_dataset(client, rand_gen):
    with pytest.raises(
            ValueError,
            match=
            "Dataset queue mode is deprecated. Please prefer Batch queue mode."
    ):
        client.create_project(
            name=rand_gen(str),
            queue_mode=QueueMode.Dataset,
        )


def test_legacy_project_dataset_relationships(project, dataset):
    assert [ds for ds in project.datasets()] == []
    assert [p for p in dataset.projects()] == []


def test_project_auto_audit_parameters(client, rand_gen):
    with pytest.raises(
            ValueError,
            match=
            "quality_mode must be set instead of auto_audit_percentage or auto_audit_number_of_labels."
    ):
        client.create_project(name=rand_gen(str), auto_audit_percentage=0.5)

    with pytest.raises(
            ValueError,
            match=
            "quality_mode must be set instead of auto_audit_percentage or auto_audit_number_of_labels."
    ):
        client.create_project(name=rand_gen(str), auto_audit_number_of_labels=2)
