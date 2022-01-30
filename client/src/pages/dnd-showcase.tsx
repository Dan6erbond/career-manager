import { Heading, VStack } from "@chakra-ui/react";
import { useCallback, useState } from "react";
import { CustomDragLayer } from "../components/dnd/CustomDragLayer";
import { ProjectListDragItem } from "../components/dnd/drag-items/ProjectListDragItem";
import { ProjectListItem } from "../components/projects/ProjectListItem";
import { DND_ITEM_TYPES } from "../lib/constants";
import { projects as projectList } from "../lib/projects";
import { Project } from "../types/Project";

export const DndShowcase = () => {
  const [projects, setProjects] = useState(projectList);

  const moveIndex = useCallback(
    (id: number, to: number) => {
      setProjects((projects) => {
        const project = projects.find((project) => project.id === id);
        const newProjects = [...projects];
        if (project !== undefined) {
          newProjects.splice(
            to,
            0,
            newProjects.splice(projects.indexOf(project), 1)[0]
          );
        }
        return newProjects;
      });
    },
    [setProjects]
  );

  return (
    <VStack spacing={4} align="stretch">
      <Heading>Projects</Heading>
      <VStack spacing={2} align="stretch">
        <CustomDragLayer
          itemLayers={[
            {
              itemType: DND_ITEM_TYPES.SHOWCASE_PROJECT_LIST_ITEM,
              render: (item: Project) => <ProjectListDragItem item={item} />,
            },
          ]}
        />
        {projects.map((project, index) => (
          <ProjectListItem
            key={project.id}
            project={project}
            moveIndex={moveIndex}
            index={index}
          />
        ))}
      </VStack>
    </VStack>
  );
};
