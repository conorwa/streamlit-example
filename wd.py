def main():
    st.title("Work Tracker App")

    work_items = []

    while True:
        st.write("## Add New Work Item")
        item_name = st.text_input("Item Name")
        item_description = st.text_area("Item Description")
        item_image = st.file_uploader("Upload Item Image", type=["jpg", "png", "jpeg"])

        if st.button("Add Item"):
            work_item = {
                "name": item_name,
                "description": item_description,
                "image": item_image,
            }
            work_items.append(work_item)

        st.write("## Work Items")
        for item in work_items:
            st.write(f"### {item['name']}")
            st.write(item['description'])
            if item['image']:
                st.image(item['image'], caption=item['name'], use_column_width=True)

        st.write("----")

if __name__ == "__main__":
    main()

