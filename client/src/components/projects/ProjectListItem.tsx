import { DragHandleIcon } from "@chakra-ui/icons";
import { Box, HStack, Text } from "@chakra-ui/react";
import { motion } from "framer-motion";
import { useEffect, useRef } from "react";
import { DropTargetMonitor, useDrag, useDrop, XYCoord } from "react-dnd";
import { getEmptyImage } from "react-dnd-html5-backend";
import { DND_ITEM_TYPES } from "../../lib/constants";
import { Project } from "../../types/Project";

interface DragItem {
  type: string;
  id: number;
  index: number;
  description: string;
}

interface ProjectListItemProps {
  project: Project;
  index: number;
  moveIndex: (id: number, to: number) => void;
}

export const ProjectListItem = ({
  project: { id, description },
  moveIndex,
  index,
}: ProjectListItemProps) => {
  const ref = useRef<HTMLDivElement>(null);

  const [{ isDragging }, dragRef, preview] = useDrag(
    () => ({
      type: DND_ITEM_TYPES.SHOWCASE_PROJECT_LIST_ITEM,
      item: () => {
        return { id, index, description };
      },
      collect: (monitor) => ({
        isDragging: monitor.isDragging(),
      }),
    }),
    []
  );

  useEffect(() => {
    preview(getEmptyImage(), { captureDraggingState: true });
  });

  const [{ handlerId }, dropRef] = useDrop({
    accept: DND_ITEM_TYPES.SHOWCASE_PROJECT_LIST_ITEM,
    collect(monitor) {
      return {
        handlerId: monitor.getHandlerId(),
      };
    },
    hover(item: DragItem, monitor: DropTargetMonitor) {
      if (!ref.current) {
        return;
      }

      const dragIndex = item.index;
      const hoverIndex = index;

      if (dragIndex === hoverIndex) {
        return;
      }

      // Determine rectangle on screen
      const hoverBoundingRect = ref.current?.getBoundingClientRect();

      // Get vertical middle
      const hoverMiddleY =
        (hoverBoundingRect.bottom - hoverBoundingRect.top) / 2;

      // Determine mouse position
      const clientOffset = monitor.getClientOffset();

      // Get pixels to the top
      const hoverClientY = (clientOffset as XYCoord).y - hoverBoundingRect.top;

      // Only perform the move when the mouse has crossed half of the items height
      // When dragging downwards, only move when the cursor is below 50%
      // When dragging upwards, only move when the cursor is above 50%

      // Dragging downwards
      if (dragIndex < hoverIndex && hoverClientY < hoverMiddleY) {
        return;
      }

      // Dragging upwards
      if (dragIndex > hoverIndex && hoverClientY > hoverMiddleY) {
        return;
      }

      moveIndex(item.id, hoverIndex);
      item.index = hoverIndex;
    },
  });

  dropRef(ref);

  return (
    <Box
      as={motion.div}
      variants={{
        static: {
          opacity: 1,
        },
        drag: {
          opacity: 0.5,
        },
      }}
      ref={ref}
      animate={isDragging ? "drag" : "static"}
      layoutId={`${DND_ITEM_TYPES.SHOWCASE_PROJECT_LIST_ITEM}-${id}`}
      rounded="md"
      shadow="md"
      p={4}
      data-handler-id={handlerId}
    >
      <HStack spacing={2}>
        <Box ref={dragRef} cursor="move">
          <DragHandleIcon />
        </Box>
        <Text>{description}</Text>
      </HStack>
    </Box>
  );
};
