<div className="content">
  {isEdit ? (
    <>
      <textarea
        value={localContent}
        onChange={(e) => setLocalContent(e.target.value)}
      />
    </>
  ) : (
    <>{content}</>
  )}</div>


{isEdit ? (
  <>
    isEdit 참일 때 보일 버튼
  </>
) : (
  <>
    false일 때 보일 버튼
  </>
)}

<DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} />