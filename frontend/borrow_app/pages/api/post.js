const posts = [
    {
      id: "post-1",
      title: "Essentials of real-time 2D",
      author: "Group-1",
      date: "Feb 21, 2023",
      summary: "Summary 1",
      image: "/path/to/image.jpg"
    },
    {
      id: "post-2",
      title: "Essentials of programming in Unity",
      author: "Group-1",
      date: "Feb 22, 2023",
      summary: "Summary 2",
      image: "/path/to/image.jpg"
    },
    {
      id: "post-3",
      title: "Publish your project",
      author: "Group-1",
      date: "Feb 21, 2023",
      summary: "Summary 3",
      image: "/path/to/image.jpg"
    }
  ];
  
  export default function handler(req, res) {
    res.status(200).json(posts);
  }
  